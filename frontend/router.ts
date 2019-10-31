import { State, PipeFn } from 'marycat'
import { pageIndex } from './pages/page-index'
import { pageAbout } from './pages/page-about'

interface Route {
  regex: RegExp
  component: (params: string[]) => PipeFn<Element>
}

const routes: Route[] = [
  {
    regex: /^$/,
    component: () => pageIndex.new(),
  }, {
    regex: /^about$/,
    component: () => pageAbout.new(),
  }
]

export const element = new State<PipeFn<Element> | null>(null)

export function update() {
  const path = location.hash.replace(/^#\/|\/$/g, '')
  const route = routes.find(x => x.regex.test(path))
  if (!route) {
    console.warn(`Unknown path: ${path}`)
    return
  }
  const [match, ...args] = path.match(route.regex) || []
  if (match) {
    element.v = route.component(args)
  }
}
