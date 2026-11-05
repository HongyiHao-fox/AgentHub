<script setup>
</script>

<template>
    <div class="hero-card">
        <p class="eyebrow">Assistant overview</p>
        <h1>Build with a calm, focused AI-style experience.</h1>
        <p class="description">
            This workspace combines a clean conversation-like UI with a simple auth flow, making it feel more like a
            modern AI product than a traditional dashboard.
        </p>

        <ul>
            <li>Simple and readable layout</li>
            <li>Friendly onboarding experience</li>
            <li>Ready for further agent features</li>
        </ul>
    </div>
</template>

<style scoped>
.hero-card {
    padding: 24px;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

h1 {
    font-size: 1.7rem;
    color: #0f172a;
    margin-bottom: 12px;
}

.description {
    color: #475569;
    margin-bottom: 16px;
}

ul {
    padding-left: 20px;
    color: #334155;
    display: grid;
    gap: 8px;
}

.eyebrow {
    text-transform: uppercase;
    letter-spacing: 0.16em;
    font-size: 0.74rem;
    font-weight: 700;
    color: #64748b;
    margin-bottom: 8px;
}
</style>