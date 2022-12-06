import Foundation

let file = "input"
var contents: [[Int]] = [[]]

guard let input = Bundle.main.url(forResource: file, withExtension: "txt") else {
    fatalError("Couldn't find \(file) in main bundle.")
}

do {
    contents = try String(contentsOf: input, encoding: .utf8)
                    .components(separatedBy: "\n\n")
                    .map({ $0.components(separatedBy: "\n")
                        .map({ Int($0)! }) 
                    })
                    
}

let calories = contents.map({ $0.reduce(0, +) })
let top3Calories = calories.sorted()[calories.endIndex-3..<calories.endIndex]
                           .reduce(0, +)

// Part 1
print(calories.max()!)

// Part 2
print(top3Calories)

