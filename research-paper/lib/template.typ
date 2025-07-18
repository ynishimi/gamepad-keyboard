#let 年月日 = "[year]年[month repr:numerical padding:none]月[day padding:none]日"
#let 年月 = "[year]年[month repr:numerical padding:none]月"
#let appendix(app) = [
  #counter(heading).update(0)
  #set heading(numbering: "A.1     ")
  #app
]
#let jarticle(
  fontsize: 11pt,
  title: none,
  authors: (),
  abstract: [],
  date: datetime.today(),
  doc,
) = {
  let roman = "Libertinus Serif"
  let mincho = "Hiragino Mincho ProN"
  let kakugothic = "Hiragino Kaku Gothic ProN"
  let math_font = "New Computer Modern Math"

  // set text(lang:"ja", font: (roman,mincho), fontsize)
  set text(lang: "ja", font: (mincho), fontsize)

  // Use A4 paper
  set page(
    paper: "a4",
    margin: auto,
    numbering: "1",
  )
  set par(justify: true)

  // 行間の調整
  set par(
    leading: 1.2em,
    justify: true,
    first-line-indent: 1.1em,
  )
  set par(spacing: 1.2em)
  show heading: set block(above: 1.6em, below: 0.6em)
  set heading(numbering: "1.1     ")
  // 様々な場所でのフォント
  show heading: set text(font: kakugothic)
  show strong: set text(font: kakugothic)
  show emph: set text(font: (roman, kakugothic))
  show math.equation: set text(font: (math_font, roman, mincho))
  // 見出しの下の段落を字下げするため
  show heading: it => {
    it
    par(text(size: 0pt, ""))
  }
  // 数式番号
  set math.equation(numbering: "(1)")
  show ref: it => {
    let eq = math.equation
    let el = it.element
    if el != none and el.func() == eq {
      // Override equation references.
      link(el.label, numbering(el.numbering, ..counter(eq).at(el.location())))
    } else {
      // Other references as usual.
      it
    }
  }
  // 目次
  show outline.entry.where(
    level: 1,
  ): it => {
    v(1.2 * fontsize, weak: true)
    it
  }
  set outline(indent: auto)

  set figure(placement: auto)
  // 図のキャプション
  // set figure(gap: 1.6em)
  show figure.caption: it => [
    #block(width: 90%, [#it])
    #v(1em)
  ]
  show figure.caption: set text(
    font: kakugothic,
    0.9 * fontsize,
  )
  // show figure.caption: set align(left)
  // タイトル
  {
    set align(center)
    text(1.5 * fontsize, font: kakugothic, strong(title))

    par(for a in authors { a })

    par(date.display(年月日))

    if abstract != [] {
      block(width: 90%, text(0.9 * fontsize, [
        *概要* \
        #align(left, abstract)
      ]))
    }
  }
  doc
}
