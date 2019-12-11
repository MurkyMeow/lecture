import ApolloClient from 'apollo-boost'

function getCookie(name: string): string {
  const entries = document.cookie.split('=')
  const idx = entries.findIndex((el, i) => i % 2 === 0 && el === name)
  return entries[idx + 1] || ''
}

export const client = new ApolloClient({
  headers: { 'X-CSRFToken': getCookie('csrftoken') },
})
