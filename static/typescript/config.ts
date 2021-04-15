export const config = {

  selector: { // our selectors for different elements
    selector:'html',
    filter: { // our selectors for filters
      selector:'.filter',
      input:{ // selectors for input wrapers element
        selector:'.filter__input',
        checkbox:{ // selector for checkbox
          selector: '.checkbox',
        }
      }
    }
  },

}
