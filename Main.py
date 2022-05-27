# TODO: 테스트 메서드 호출하기
# TODO: 먼저 setUp 호출하기
# TODO: 나중에 tearDown 호출하기
# TODO: 테스트 메서드가 실패하더라도 tearDown 호출하기
# TODO: 여러 개의 테스트 실행하기
# TODO: 수집된 결과를 출력하기

class WasRun:
    def __init__(self, name):
        self.wasRun = None

    def testMethod(self):
        self.wasRun = 1

test = WasRun('testMethod')
print(test.wasRun)
test.testMethod()
print(test.wasRun)
