# In codingbat_app/views.py

def string_splosion(request, word):
    def string_splosion_solution(s):
        result = ""
        for i in range(len(s) + 1):
            result += s[:i]
        return result

    response_data = {
        "input": word,
        "expected_output": string_splosion_solution(word),
        "test_cases": [
            {"input": "Code", "output": string_splosion_solution("Code")},
            {"input": "abc", "output": string_splosion_solution("abc")},
            {"input": "ab", "output": string_splosion_solution("ab")}
        ]
    }
    return JsonResponse(response_data)




def cat_dog(request, s):
    def cat_dog_solution(s):
        return s.count("cat") == s.count("dog")

    response_data = {
        "input": s,
        "expected_output": cat_dog_solution(s),
        "test_cases": [
            {"input": "catdog", "output": cat_dog_solution("catdog")},
            {"input": "catcat", "output": cat_dog_solution("catcat")},
            {"input": "1cat1cadodog", "output": cat_dog_solution("1cat1cadodog")}
        ]
    }
    return JsonResponse(response_data)




def lone_sum(request, a, b, c):
    def lone_sum_solution(a, b, c):
        if a == b == c:
            return 0
        elif a == b:
            return c
        elif a == c:
            return b
        elif b == c:
            return a
        else:
            return a + b + c

    response_data = {
        "input": (a, b, c),
        "expected_output": lone_sum_solution(a, b, c),
        "test_cases": [
            {"input": (1, 2, 3), "output": lone_sum_solution(1, 2, 3)},
            {"input": (3, 2, 3), "output": lone_sum_solution(3, 2, 3)},
            {"input": (3, 3, 3), "output": lone_sum_solution(3, 3, 3)}
        ]
    }
    return JsonResponse(response_data)
