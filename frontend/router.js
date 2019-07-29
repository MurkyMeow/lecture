const routes = [
  {
    regex: /^$/,
    component: 'melior-page-index',
  },
  {
    regex: /^about$/,
    component: 'melior-page-about',
  }
]

let query = {}

export function get_query() {
  return query
}
export function update() {
  const path = location.hash.replace(/^#\/|\/$/g, '')
  const route = routes.find(x => x.regex.test(path))
  if (!route) {
    console.warn(`Unknown path: ${path}`)
    return
  }
  const [_, ...args] = path.match(route.regex) || []
  const $el = document.createElement(route.component)
  const { firstChild } = document.body
  if (firstChild) {
    firstChild.replaceWith($el)
  } else {
    document.body.appendChild($el)
  }
  if (route.params) {
    query = {}
    route.params.forEach((param, i) => query[param] = args[i])
  }
}
window.onhashchange = update