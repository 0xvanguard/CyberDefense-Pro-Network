import DefaultTheme from 'vitepress/theme'
import LabTerminal from '../components/LabTerminal.vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('LabTerminal', LabTerminal)
  }
}
