import { State, customElement, PipeFn, styleEl, repeat, style } from 'marycat'
import { div, h1, article, section, pre } from '../bindings'
import { Progress } from '../components/progress'
import { Button } from '../components/button'
import { get } from '../api'
import css from './page-index.css'

interface Lecture {
  id: number
  title: string
  subtitle: string
  background: string
}
interface Course {
  id: number
  name: string
}

const view_lecture = (item: State<Lecture>) =>
  (div('.lecture')
    (div('.lecture-info')
      (style('background', item._.background))
      (div('.lecture-title')(item._.title))
      (pre('.lecture-summary')(item._.subtitle))
    )
    (Progress.new()
      (Progress.prop('max', 5))
      (Progress.prop('done', [0, 2])
    ))
  )

function viewPageIndex(h: PipeFn<ShadowRoot>) {
  const courses = new State<Course[]>([])
  get<Course[]>('/course/courses')
    .then(data => courses.v = data)
  return h
  (styleEl()(css))
  (div('.content')
    (repeat(courses, x => x.id.toString(), course =>
      (article()
        (h1()(course._.name))
        // (section().repeat(courses._.key, x => x, (item, i) =>
        //   view_lecture(item).on('click', () => {
        //     lecture.v = { ...item.v, name: key.v, index: i.v }
        //   })
        // ))
      )
    ))
    (Button.new('.link', 'Показать все'))
  )
}
export const pageIndex = customElement('lecture-page-index', viewPageIndex)
