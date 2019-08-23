import { State, webc, iter, _if } from 'marycat'
import { Button } from '../components/button'
import { Lesson } from '../components/lesson';
import { Progress } from '../components/progress';
import { get } from '../api'
import css from './page-index.css'

const view_lecture = (item, click) =>
  (div('.lecture').click(click)
    (div('.lecture-info').style('background', item._`background`)
      (div('.lecture-title')(item._`title`.or('')))
      (pre('.lecture-summary')(item._`subtitle`.or('')))
    )
    (Progress().max(5).done([0, 2]))
  )

export const pageIndex = webc('lecture-page-index', {
  css,
  render(h) {
    const lecture = new State(null)
    const courses = new State({})
    get('/static/preview.json').then(data => courses.v = data)
    return h
    (div('.content')
      (_if(lecture)
        (Lesson().data(lecture).on('hide', () => lecture.v = null))
      )
      (iter(courses.keys, key =>
        (article()
          (h1(key))
          (section()
            (iter(courses._`${key}`, (item, i) =>
              view_lecture(item, () => lecture.v = { ...item.v, name: key.v, index: i.v })
            ))
          )
        )
      ))
      (Button('.link').text('Показать все'))
    )
  },
})
