import { State } from 'marycat'
import { pageIndex } from './pages/page-index'
import { pageAbout } from './pages/page-about'

const routes = [
  {
    regex: /^$/,
    component: pageIndex,
  }, {
    regex: /^about$/,
    component: pageAbout,
  }
]

let query = {}

export const element = new State()
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
  if (route.params) {
    query = {}
    route.params.forEach((param, i) => query[param] = args[i])
  }
  element.v = route.component
}
window.onhashchange = update