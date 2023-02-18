def inclu_check(cards, card_num, test):
    start = 0
    end = card_num - 1
    
    result = 0
    
    while start <= end:
        mid = (start + end) // 2
        
        if cards[mid] == test:
            result = 1
            return result
        
        elif cards[mid] > test:
            start = start
            end = mid - 1
            
        elif cards[mid] < test:
            start = mid + 1
            end = end
            
    return result

card_num = int(input())
cards = list(map(int, input().split()))
    
test_num = int(input())
tests = list(map(int, input().split()))

cards.sort()

for test in tests:
    result = inclu_check(cards, card_num, test)
    print(result, end = ' ')