import { State, customElement, PipeFn, styleEl, on, attr, cx, name } from 'marycat'
import { form, div, input, button } from '../bindings'
import { Toggle } from './toggle'
import { Button } from './button'
import { store } from '../store'
import * as api from '../api'
import css from './form-auth.css'

type FormMode = '🔑' | '👽'

function viewFormAuth(h: PipeFn<ShadowRoot>) {
  const option: State<FormMode> = new State('🔑')
  const errors = new State({ main: '', email: '', name: '' })
  const submit = async (e: Event) => {
    const url = `/auth/${option.v === '👽' ? 'signup' : 'signin'}/`
    try {
      errors.v = { main: '', email: '', name: '' }
      const rawdata = new FormData(e.target as HTMLFormElement)
      const data = Object.fromEntries(rawdata)
      store.user.v = await api.post(url, data)
    } catch (err) {
      if (err.status === 404) {
        errors.v = { ...errors.v, main: 'Неверный логин или пароль' }
      } else if (err.status === 409) {
        const conflict = await err.json()
        if (conflict.email) errors.v = { ...errors.v, email: 'Email занят' }
        if (conflict.name) errors.v = { ...errors.v, name: 'Никнейм занят' }
      } else {
        errors.v = { ...errors.v, main: 'Не удаётся войти' }
      }
    }
  }
  return h
  (styleEl(css))
  (form()
    (on('submit', submit, { prevent: true }))
    (div(cx`error`)(errors._.main.or('')))
    (Toggle.new()
      (Toggle.prop('tabs', ['🔑', '👽']))
      (Toggle.on('change', e => option.v = <FormMode>e.detail))
    )
    (input(name`email`)
      (attr('type', 'email'))
      (attr('placeholder', 'Email'))
      (attr('required', true))
      ((el: HTMLInputElement) => errors.sub(v => el.setCustomValidity(v.email)))
    )
    (input(name`passwor`)
      (attr('type', 'password'))
      (attr('placeholder', 'Пароль'))
      (attr('required', true))
    )
    (option.map(v => v === '👽' &&
      (input(name`password_again`)
        (attr('type', 'password'))
        (attr('placeholder', 'Повторите пароль'))
        (attr('required', true))
      )
      (input(name`name`)
        (attr('placeholder', 'Никнейм'))
        (attr('required', true))
        ((el: HTMLInputElement) => errors.sub(v => el.setCustomValidity(v.name)))
      )
    ))
    (button()
      (Button.new('Продолжить'))
    )
  )
}
export const FormAuth = customElement('lecture-form-auth', viewFormAuth)
