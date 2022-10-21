module tests

open NUnit.Framework
open ocr

[<Literal>]
let one =
    """
   
  |
  |

"""

[<SetUp>]
let Setup () =
    ()

[<Test>]
let ParsingEmptyInputShouldReturnNone () =
    let actual = parse ""
    Assert.AreEqual(None, actual)

[<Test>]
let parseSingleCharacterOne () =
    let actual = parse one
    Assert.AreEqual(Some 1 , actual)