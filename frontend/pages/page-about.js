import { webc } from 'marycat'

export const pageAbout = webc({
  name: 'lecture-page-about',
  render: h => (h
    (div('About page!'))
  ),
})
