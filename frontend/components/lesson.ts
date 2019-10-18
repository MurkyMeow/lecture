import { State, customElement, PipeFn, defAttr, styleEl, on, dispatch, attr, repeat } from 'marycat'
import { iframe, div, textarea, img } from '../bindings'
import { Progress } from './progress'
import { Button } from './button'
import css from './lesson.css'

const comments = new State([
  {
    user: { name: 'rulon oboev', photo: '' },
    text: 'cool',
  },
  {
    user: { name: 'fabric zavodov', photo: '' },
    text: 'fancy',
  },
])

function viewLesson(h: PipeFn, {
  slide = defAttr(0),
  data = defAttr({ name: '', index: 0 })
}) {
  const { name, index } = data.v
  const slides = new State(0)
  const onload = async (e: Event) => {
    // await target.contentWindow!.load
    // slides.v = target.contentWindow!.slides.length
  }
  return h
  (on('click', () => {
    h(dispatch('hide', null))
  }))
  (styleEl()(css))
  (div('.wrapper')
    (on('click', _=>_, { stop: true }))
    (attr('tabindex', 0))
    (on('keydown', (e: Event) => {
      switch ((<KeyboardEvent>e).code) {
        case 'ArrowLeft': return slide.v > 0 && slide.v--
        case 'ArrowRight': return slide.v < slides.v - 1 && slide.v++
      }
    }))
    (div('.content')
      (Progress.new()
        (Progress.prop('max', slides))
        (Progress.prop('active', slide))
        (on('change', (e: Event) => slide.v = (<CustomEvent>e).detail))
      )
      (iframe()
        (on('load', onload))
        (attr('height', '300px'))
        (attr('src', slide.map(v => `/course/${name}/${index + 1}/#${v}`)))
      )
    )
    (div('.comment-box')
      (div('.comment-input')
        (textarea()(attr('placeholder', 'Оставить комментарий')))
        (Button.new('📡'))
      )
      (repeat(comments, x => x, x =>
        (div('.comment')
          (img()(attr('src', x._.user._.photo)))
          (div()
            (div('.comment-author')(x._.user._.name))
            (div('.comment-text')(x._.text))
          )
        )
      ))
    )
  )
}
export const Lesson = customElement('lecture-lesson', viewLesson)
