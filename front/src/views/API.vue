<script setup>
import { ref } from 'vue'

const api = ref('')
</script>

<template>
    <div class="api-card">
        <p class="eyebrow">API setup</p>
        <h2>Connect your model provider</h2>
        <p class="description">Add your API key to enable agent actions and extended integrations.</p>

        <label>
            <span>API key</span>
            <input v-model="api" type="password" placeholder="Paste your API key" />
        </label>
    </div>
</template>

<style scoped>
.api-card {
    margin-top: 16px;
    padding: 20px;
    border: 1px solid rgba(15, 23, 42, 0.08);
    border-radius: 20px;
    background: #f8fbff;
}

h2 {
    font-size: 1.12rem;
    color: #0f172a;
    margin-bottom: 8px;
}

.description {
    color: #64748b;
    margin-bottom: 12px;
}

.eyebrow {
    text-transform: uppercase;
    letter-spacing: 0.16em;
    font-size: 0.7rem;
    font-weight: 700;
    color: #64748b;
    margin-bottom: 8px;
}

label {
    display: flex;
    flex-direction: column;
    gap: 8px;
    color: #334155;
}

input {
    border: 1px solid #dbe3ef;
    border-radius: 12px;
    padding: 11px 12px;
    background: #fff;
}
</style>