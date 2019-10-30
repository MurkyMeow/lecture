function get_cookie(name: string): string {
  const entries = document.cookie.split('=')
  const idx = entries.findIndex((el, i) => i % 2 === 0 && el === name)
  return entries[idx + 1] || ''
}

const req = (method: string) => <T>(url: string, body?: object): Promise<T> =>
  fetch(url, {
    credentials: 'include',
    method,
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': get_cookie('csrftoken'),
    },
    body: JSON.stringify(body) || undefined,
  }).then(res => {
    if (!res.ok) throw res.statusText || res.status
    return res.json()
  })

export const get = req('GET')
export const del = req('DEL')
export const put = req('PUT')
export const post = req('POST')
export const patch = req('PATCH')
