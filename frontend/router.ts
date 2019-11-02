import { State, PipeFn } from 'marycat'
import { pageIndex } from './pages/page-index'
import { pageAbout } from './pages/page-about'
import { PageLesson } from './pages/page-lesson'

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
  }, {
    regex: /^lesson\/(\d+)\/(\d+)$/,
    component: ([lessonId, slideId]) => (PageLesson.new()
      (PageLesson.prop('slideId', Number(slideId)))
      (PageLesson.prop('lessonId', Number(lessonId)))
    ),
  },
]

export const element = new State<PipeFn<Element> | null>(null)

export function update() {
  const path = location.hash.replace(/^#\/|\/$/g, '')
  for (const route of routes) {
    const [match, ...args] = path.match(route.regex) || []
    if (match !== undefined) {
      return element.v = route.component(args)
    }
  }
}
