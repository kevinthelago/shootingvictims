<template>
  <div class="person-item">
    <span class="name">{{ fullName }}</span>
    <span class="date">{{ person.dateOfDeath }}</span>
  </div>
</template>

<script>
export default {
  name: 'Victim',
  props: {
    person: {
      type: Object,
      required: true
    }
  },
  computed: {
    fullName() {
      const { firstname, middlename, lastname } = this.person
      const middle = middlename ? ` ${middlename} ` : ' '
      return `${firstname}${middle}${lastname}`
    }
  }
}
</script>

<style scoped>
.person-item {
  padding: 15px;
  border-bottom: 1px solid #333;
  font-size: 1.2rem;
  transition: background-color 0.3s ease;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.name {
  flex: 1;
}

.date {
  text-align: right;
}

.person-item:hover {
  background-color: #111;
}

.person-item:last-child {
  border-bottom: none;
}
</style>