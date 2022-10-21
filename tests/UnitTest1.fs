module tests

open NUnit.Framework
open ocr


[<SetUp>]
let Setup () =
    ()

[<Test>]
let ParsingEmptyInputShouldReturnNone () =
    let actual = parse ""
    Assert.AreEqual(None, actual)
