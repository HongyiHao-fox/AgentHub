<script setup>
</script>

<template>
    <header class="header">
        <div>
            <p class="eyebrow">Agent experience</p>
            <h1>Agent Hub</h1>
        </div>

        <div class="badges">
            <span class="badge">ChatGPT-style UI</span>
            <span class="badge">Flask ready</span>
        </div>
    </header>
</template>

<style scoped>
.header {
    max-width: 1200px;
    margin: 0 auto;
    padding: 24px 24px 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
}

h1 {
    font-size: 1.6rem;
    color: #0f172a;
}

.eyebrow {
    text-transform: uppercase;
    letter-spacing: 0.16em;
    font-size: 0.7rem;
    font-weight: 700;
    color: #64748b;
    margin-bottom: 4px;
}

.badges {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.badge {
    padding: 8px 12px;
    border-radius: 999px;
    background: #eef2ff;
    color: #4338ca;
    font-size: 0.85rem;
    font-weight: 600;
}

@media (max-width: 700px) {
    .header {
        flex-direction: column;
        align-items: flex-start;
    }
}
</style>