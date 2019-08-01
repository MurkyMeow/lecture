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
  body: JSON.stringify(body),
  ...opts,
})

const patch = (url, body) =>
  post(url, body, { method: 'PATCH' })

const put = (url, body) =>
  post(url, body, { method: 'PUT' })

export { get, post, put, patch, del }
