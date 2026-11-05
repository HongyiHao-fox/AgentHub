<script setup>
import { reactive, ref } from 'vue'
import Header from './components/Header.vue'
import Home from './views/Home.vue'
import API from './views/API.vue'

const mode = ref('login')
const form = reactive({ username: '', password: '' })
const status = ref('')
const loading = ref(false)

function setMode(nextMode) {
  mode.value = nextMode
  status.value = ''
}

async function submit() {
  loading.value = true
  status.value = ''

  try {
    const endpoint = mode.value === 'login' ? '/auth/login' : '/auth/register'
    const response = await fetch(`http://127.0.0.1:5000${endpoint}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.error || '请求失败')
    }

    status.value = data.message || '操作成功'
  } catch (error) {
    status.value = error.message
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="app-shell">
    <Header />

    <main class="workspace">
      <section class="hero-panel">
        <Home />
      </section>

      <section class="control-panel">
        <div class="section-card auth-card">
          <div class="section-heading">
            <div>
              <p class="eyebrow">Access</p>
              <h2>{{ mode === 'login' ? 'Welcome back' : 'Create your account' }}</h2>
            </div>

            <div class="toggle">
              <button :class="{ active: mode === 'login' }" @click="setMode('login')">Login</button>
              <button :class="{ active: mode === 'register' }" @click="setMode('register')">Register</button>
            </div>
          </div>

          <form class="auth-form" @submit.prevent="submit">
            <label>
              <span>Username</span>
              <input v-model="form.username" placeholder="Enter your username" required />
            </label>

            <label>
              <span>Password</span>
              <input v-model="form.password" type="password" placeholder="Enter your password" required />
            </label>

            <button class="primary-btn" type="submit" :disabled="loading">
              {{ loading ? 'Processing...' : mode === 'login' ? 'Sign in' : 'Create account' }}
            </button>
          </form>

          <p v-if="status" class="status" :class="{ error: status.includes('失败') || status.includes('错误') }">
            {{ status }}
          </p>
        </div>

        <API />
      </section>
    </main>
  </div>
</template>

<style scoped>
.app-shell {
  min-height: 100vh;
  width: 100%;
  background: linear-gradient(135deg, #f8fbff 0%, #f3f7ff 100%);
}

.workspace {
  max-width: 1200px;
  margin: 0 auto;
  padding: 24px;
  display: grid;
  gap: 24px;
  grid-template-columns: 1.05fr 0.95fr;
}

.hero-panel,
.section-card {
  border: 1px solid rgba(15, 23, 42, 0.08);
  background: rgba(255, 255, 255, 0.9);
  border-radius: 24px;
  box-shadow: 0 20px 45px rgba(15, 23, 42, 0.06);
  backdrop-filter: blur(18px);
}

.section-card {
  padding: 24px;
}

.section-heading {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-bottom: 20px;
}

.eyebrow {
  text-transform: uppercase;
  letter-spacing: 0.16em;
  font-size: 0.74rem;
  font-weight: 700;
  color: #64748b;
  margin-bottom: 6px;
}

h2 {
  font-size: 1.3rem;
  color: #0f172a;
}

.toggle {
  display: flex;
  gap: 8px;
  padding: 4px;
  border-radius: 999px;
  background: #f1f5f9;
}

.toggle button {
  border: none;
  background: transparent;
  color: #475569;
  padding: 8px 12px;
  border-radius: 999px;
  cursor: pointer;
  font-weight: 600;
}

.toggle button.active {
  background: #111827;
  color: #fff;
}

.auth-form {
  display: flex;
  flex-direction: column;
  gap: 14px;
}

label {
  display: flex;
  flex-direction: column;
  gap: 8px;
  font-size: 0.92rem;
  color: #334155;
}

input {
  border: 1px solid #dbe3ef;
  background: #fbfdff;
  border-radius: 12px;
  padding: 12px 14px;
  outline: none;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

input:focus {
  border-color: #4f46e5;
  box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.12);
}

.primary-btn {
  border: none;
  border-radius: 12px;
  padding: 12px 16px;
  background: linear-gradient(135deg, #4f46e5, #2563eb);
  color: #fff;
  font-weight: 700;
  cursor: pointer;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.primary-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 20px rgba(79, 70, 229, 0.2);
}

.primary-btn:disabled {
  opacity: 0.7;
  cursor: wait;
}

.status {
  margin-top: 16px;
  padding: 12px 14px;
  border-radius: 12px;
  background: #ecfdf5;
  color: #047857;
}

.status.error {
  background: #fef2f2;
  color: #b91c1c;
}

@media (max-width: 900px) {
  .workspace {
    grid-template-columns: 1fr;
  }
}
</style>
