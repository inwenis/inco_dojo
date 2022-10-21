module ocr

[<Literal>]
let one =
    """
   
  |
  |

"""

let parse (input: string)  =
    if input = one then Some 1
    else None
