import { State, PipeFn } from 'marycat'
import { pageIndex } from './pages/page-index'
import { pageAbout } from './pages/page-about'

type Route = {
  regex: RegExp
  params?: string[]
  component: () => PipeFn
}

const routes: Route[] = [
  {
    regex: /^$/,
    component: pageIndex.new,
  }, {
    regex: /^about$/,
    component: pageAbout.new,
  }
]

let query: { [x: string]: string } = {}
export const get_query = () => query
export const element = new State<PipeFn | null>(null)

export function update() {
  const path = location.hash.replace(/^#\/|\/$/g, '')
  const route = routes.find(x => x.regex.test(path))
  if (!route) {
    console.warn(`Unknown path: ${path}`)
    return
  }
  if (route.params) {
    query = {}
    const [_, ...args] = path.match(route.regex) || []
    route.params.forEach((param, i) => query[param] = args[i])
  }
  element.v = route.component()
}
