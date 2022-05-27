# TODO: 나중에 tearDown 호출하기
# TODO: 테스트 메서드가 실패하더라도 tearDown 호출하기
# TODO: 여러 개의 테스트 실행하기
# TODO: 수집된 결과를 출력하기

class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        self.setUp()
        method = getattr(self, self.name)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None
        self.wasSetup = 1

    def testMethod(self):
        self.wasRun = 1

class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testSetup(self):
        self.test.run()
        assert(self.test.wasSetup)

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun)

TestCaseTest("testRunning").run()
TestCaseTest("testSetup").run()
