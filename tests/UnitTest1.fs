module tests

open NUnit.Framework
open ocr
open Characters

[<Test>]
let ParsingEmptyInputShouldReturnNone () =
    let actual = parse ""
    Assert.AreEqual(None, actual)

[<TestCase(one, 1)>]
[<TestCase(two, 2)>]
[<TestCase(three, 3)>]
[<TestCase(four, 4)>]
[<TestCase(five, 5)>]
[<TestCase(six, 6)>]
[<TestCase(seven, 7)>]
[<TestCase(eight, 8)>]
[<TestCase(nine, 9)>]
[<TestCase(zero, 0)>]
let parseSingleCharacter (input, expected) =
    let actual = parse input
    Assert.AreEqual(Some expected, actual)