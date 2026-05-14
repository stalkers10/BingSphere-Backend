import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { finalize } from 'rxjs';
import { AuthService } from '../../services/auth';
import { Router } from '@angular/router';
import { FooterComponent } from '../footer/footer';

@Component({
  selector: 'app-auth',
  imports: [CommonModule, FormsModule, FooterComponent],
  templateUrl: './auth.html',
  styleUrl: './auth.scss',
})
export class AuthComponent {
  isLogin = true;
  username = '';
  password = '';
  email = '';
  showPassword = false;
  isSubmitting = false;
  feedbackMessage: string | null = null;
  feedbackTone: 'success' | 'error' = 'success';

  constructor(private auth: AuthService, private router: Router) {}

  submit() {
    if (this.isSubmitting) {
      return;
    }

    const username = this.username.trim();
    const password = this.password;
    const email = this.email.trim();

    if (!username || !password || (!this.isLogin && !email)) {
      this.setFeedback('Fill in all required fields before continuing.', 'error');
      return;
    }

    this.isSubmitting = true;
    this.feedbackMessage = null;

    if (this.isLogin) {
      this.auth.login({ username, password })
        .pipe(finalize(() => {
          this.isSubmitting = false;
        }))
        .subscribe({
          next: () => this.router.navigate(['/home']),
          error: (err) => {
            this.setFeedback(this.extractError(err, 'Login failed. Please check your credentials.'), 'error');
          }
        });
    } else {
      this.auth.register({ username, password, email })
        .pipe(finalize(() => {
          this.isSubmitting = false;
        }))
        .subscribe({
          next: () => {
            this.isLogin = true;
            this.password = '';
            this.showPassword = false;
            this.setFeedback('Account created successfully. Sign in with your new credentials.', 'success');
          },
          error: (err) => {
            this.setFeedback(this.extractError(err, 'Registration failed. Please try again.'), 'error');
          }
        });
    }
  }

  toggleMode() {
    this.isLogin = !this.isLogin;
    this.password = '';
    this.showPassword = false;
    this.feedbackMessage = null;
  }

  private setFeedback(message: string, tone: 'success' | 'error') {
    this.feedbackMessage = message;
    this.feedbackTone = tone;
  }

  private extractError(err: any, fallback: string) {
    const payload = err?.error;

    if (typeof payload === 'string') {
      return payload;
    }

    if (payload?.detail && typeof payload.detail === 'string') {
      return payload.detail;
    }

    if (payload?.error && typeof payload.error === 'string') {
      return payload.error;
    }

    if (payload && typeof payload === 'object') {
      const firstEntry = Object.entries(payload)[0];

      if (firstEntry) {
        const [, value] = firstEntry;

        if (Array.isArray(value) && value.length) {
          return String(value[0]);
        }

        if (typeof value === 'string') {
          return value;
        }
      }
    }

    return fallback;
  }
}
