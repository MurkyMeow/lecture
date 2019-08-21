function get_cookie(name) {
  const entries = document.cookie.split('=')
  const idx = entries.findIndex((el, i) => i % 2 === 0 && el === name)
  return entries[idx + 1] || null
}

const get = (url, opts = {}) =>
  fetch(url, {
    credentials: 'include',
    method: 'GET',
    headers: { 'Content-Type': 'application/json' },
    ...opts,
  }).then(res => {
    if (!res.ok) throw res;
    return res.json();
  });

const del = url =>
  get(url, { method: 'DELETE' })

const post = (url, body, opts = {}) => get(url, {
  method: 'POST',
  body: JSON.stringify({
    ...body,
    csrfmiddlewaretoken: get_cookie('csrftoken'),
  }),
  ...opts,
})

const patch = (url, body) =>
  post(url, body, { method: 'PATCH' })

const put = (url, body) =>
  post(url, body, { method: 'PUT' })

export { get, post, put, patch, del }
