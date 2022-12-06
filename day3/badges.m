#import <Foundation/Foundation.h>

int main(int argc, const char *argv[]) {
    NSString *path = [[NSBundle mainBundle] pathForResource:@"input" ofType:NULL];
    NSString *content = [NSString stringWithContentsOfFile:path 
                                                    encoding:NSUTF8StringEncoding 
                                                        error:NULL];

    // BEGIN PART 1                               
    NSArray *rucksacks = [content componentsSeparatedByString:@"\n"];
    NSString *comp1 = [[NSMutableString alloc] init];
    NSString *comp2 = [[NSMutableString alloc] init];
    NSMutableArray *commonItems = [NSMutableArray array];

    for (id sack in rucksacks) {
        comp1 = [sack substringToIndex:[sack length]/2];
        comp2 = [sack substringFromIndex:[sack length]/2];

        NSMutableArray *comp1Chars = [NSMutableArray array];
        NSMutableArray *comp2Chars = [NSMutableArray array];
        
        [comp1 enumerateSubstringsInRange:[comp1 rangeOfString:comp1]
                                    options:NSStringEnumerationByComposedCharacterSequences
                                usingBlock:^(NSString *substring, NSRange substringRange, NSRange enclosingRange, BOOL *stop) {
                                [comp1Chars addObject:substring];
                                }];

        [comp2 enumerateSubstringsInRange:[comp2 rangeOfString:comp2]
                                    options:NSStringEnumerationByComposedCharacterSequences
                                usingBlock:^(NSString *substring, NSRange substringRange, NSRange enclosingRange, BOOL *stop) {
                                [comp2Chars addObject:substring];
                                }];

        NSMutableSet *common = [[NSMutableSet alloc] initWithArray:comp1Chars];
        [common intersectSet:[[NSMutableSet alloc] initWithArray:comp2Chars]];
        [commonItems addObjectsFromArray:[common allObjects]];
    }

    int sum = 0;
    for (id item in commonItems) {
        int ascii = [item characterAtIndex:0];

        if (ascii <= 97) {
            sum += ascii - (int)'A' + 27;
        } else {
            sum += ascii - (int)'a' + 1;
        }
    }

    NSLog(@"%d", sum);

    // BEGIN PART 2
    NSMutableArray *groups = [NSMutableArray array];
    NSMutableIndexSet *indexSet = [[NSMutableIndexSet alloc] init];
    for (int i = 0; i < [rucksacks count]; i+=3) {
        [indexSet removeAllIndexes];
        [indexSet addIndexesInRange:NSMakeRange(i,3)];
        [groups addObject:[rucksacks objectsAtIndexes:indexSet]];
    }

    NSMutableArray *badges = [NSMutableArray array];
    for (id group in groups) {
        NSMutableArray *comp1Chars = [NSMutableArray array];
        NSMutableArray *comp2Chars = [NSMutableArray array];
        NSMutableArray *comp3Chars = [NSMutableArray array];
        
        [group[0] enumerateSubstringsInRange:[group[0] rangeOfString:group[0]]
                                    options:NSStringEnumerationByComposedCharacterSequences
                                usingBlock:^(NSString *substring, NSRange substringRange, NSRange enclosingRange, BOOL *stop) {
                                [comp1Chars addObject:substring];
                                }];

        [group[1] enumerateSubstringsInRange:[group[1] rangeOfString:group[1]]
                                    options:NSStringEnumerationByComposedCharacterSequences
                                usingBlock:^(NSString *substring, NSRange substringRange, NSRange enclosingRange, BOOL *stop) {
                                [comp2Chars addObject:substring];
                                }];

        [group[2] enumerateSubstringsInRange:[group[2] rangeOfString:group[2]]
                                    options:NSStringEnumerationByComposedCharacterSequences
                                usingBlock:^(NSString *substring, NSRange substringRange, NSRange enclosingRange, BOOL *stop) {
                                [comp3Chars addObject:substring];
                                }];

        NSMutableSet *common = [[NSMutableSet alloc] initWithArray:comp1Chars];
        [common intersectSet:[[NSMutableSet alloc] initWithArray:comp2Chars]];
        [common intersectSet:[[NSMutableSet alloc] initWithArray:comp3Chars]];
        [badges addObjectsFromArray:[common allObjects]];
    }

    sum = 0;
    for (id badge in badges) {
        int ascii = [badge characterAtIndex:0];

        if (ascii <= 97) {
            sum += ascii - (int)'A' + 27;
        } else {
            sum += ascii - (int)'a' + 1;
        }
    }

    NSLog(@"%d", sum);

    return 0;
}