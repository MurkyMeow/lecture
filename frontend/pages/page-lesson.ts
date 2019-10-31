import { State, customElement, PipeFn, styleEl, on, attr, repeat, defAttr } from 'marycat'
import { iframe, div, textarea, img } from '../bindings'
import { Progress } from '../components/progress'
import { Button } from '../components/button'
import css from './page-lesson.css'

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

function viewLesson(h: PipeFn<ShadowRoot>, {
  lessonId = defAttr(0),
  slideId = defAttr(0),
}) {
  const slides = new State(0)
  const onload = async (e: Event) => {
    // await target.contentWindow!.load
    // slides.v = target.contentWindow!.slides.length
  }
  return h
  (styleEl()(css))
  (on('keydown', (e: Event) => {
    switch ((<KeyboardEvent>e).code) {
      case 'ArrowLeft': return slideId.v > 0 && slideId.v--
      case 'ArrowRight': return slideId.v < slides.v - 1 && slideId.v++
    }
  }))
  (Progress.new()
    (Progress.prop('max', slides))
    (Progress.prop('active', slideId))
    (on('change', (e: Event) => slideId.v = (<CustomEvent>e).detail))
  )
  (iframe()
    (on('load', onload))
    (attr('height', '300px'))
    // (attr('src', slideId.map(v => `/course/${name}/${index + 1}/#${v}`)))
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
}
export const PageLesson = customElement('lecture-lesson', viewLesson)
