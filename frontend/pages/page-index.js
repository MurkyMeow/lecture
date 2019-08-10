import { webc } from 'marycat'
import { Button } from '../components/button'
import { Lesson } from '../components/lesson';
import { Progress } from '../components/progress';
import css from './page-index.css'

const lecture = (title = '', summary = '') =>
  (div('.lecture')
    (div('.lecture-info')
      (div('.lecture-title')(title))
      (div('.lecture-summary')(summary))
    )
    (Progress().max(5).done([0, 2]))
  )

export const pageIndex = webc('lecture-page-index', {
  css,
  render: h => (h
    (div('.content')
      (Lesson())
      (h1('Линейная алгебра (0 / 20)'))
      (section()
        (lecture('В жизни не пригодится?', 'Мотивация, примеры'))
        (lecture('Что такое вектор', '(🐺, 🐐, 🥦)'))
        (lecture('Что такое матрица', [
          div('(1, 0, 1)'),
          div('(️0, 1, 1)'),
          div('(️1, 1, 0)'),
        ]))
      )
      (Button()('.link').text('Показать все'))
      (h1('Дискретный анализ (0 / 15)'))
      (section()
        (lecture())
        (lecture())
      )
    )
  ),
})
