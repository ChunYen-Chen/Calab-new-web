## Website
[CA Lab Website](https://chunyen-chen.github.io/Calab-new-web.github.io/)


## Reference
1. [Original reference](https://github.com/learning-zone/website-templates)
1. [Font Awesome](https://fontawesome.com/v6/download)


## Maintenance
1. Rules of the home page
   * less than 5 news (news in home should be happened in previous year or this year)
   * less than 12 members
   * less than 5 publications
   * less than 6 courses

1. Add a new publication
   * Use the `script/bib2html.py`

1. Picture size
   * Sponser picture size: 200x50
   * Project picture size: 400x289 / 600x450
   * Member  picture size: 225x225 (best), or a square img (size can be random)

1. Add a new member
   * Image size
   * links
   * set the id and class

1. Minify the CSS
   * use the `script/minifyCSS.py` (not tested yet)

## Known bugs
1. `background-attachment: fixed;` does not work on any ios devices. See [here](https://caniuse.com/?search=background-attachment%3A).
One possible [solution](https://stackoverflow.com/questions/26372127/background-fixed-no-repeat-not-working-on-mobile)?

## Tips
1. Add a Greeks character in HTML.
   * [website](https://www.thoughtco.com/html-codes-greek-characters-4062212)

1. Check if the CSS parameter is available across all devices
   * [Can I Use](https://caniuse.com/)

## TODO
### Fix
* fix the small width layout
* let the content change width to be a variable in css (complex!!!)
* check the mobile version (include the css setting)
* Try to let the background of contact to be fixed

### Warning
* clean the warning from the map

### Before to go
* clean all the empty links
* link all the members to their section in member page
* Add the readme or instruction about the maintenance of website
* fill the words which need to be filled

### Optimizations
* check the figure of project and member => use github workflow?
* the publication filters initialized as hide but still show at start
* Redesign the first page
* sort button of publucation?
* a fold navbar e.g. (member => prof, RA, PHD...)
* fill term of use and privacy policy at footer [This](https://www.termsofusegenerator.net) and  [This](https://termify.io/privacy-policy-generator?gad_source=1&gclid=CjwKCAiAopuvBhBCEiwAm8jaMSbkpk0Mk7J4fZngmu3RuioKEHaxlYKaBKgx_55PW-REAaizBIze5BoC0NIQAvD_BwE)
* re-layout the footer
* optimize the load speed (https://pagespeed.web.dev/ or use the Edge insight)
* share the footer and the header
