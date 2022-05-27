# TODO: 테스트 메서드가 실패하더라도 tearDown 호출하기
# TODO: 여러 개의 테스트 실행하기
# TODO: setUp 에러를 잡아서 보고하기

class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.failureCount += 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.failureCount) 

class TestCase:
    def __init__(self, name):
        self.name = name

    def setUp(self):
        pass

    def run(self):
        result = TestResult()
        result.testStarted()
        self.setUp()
        try:
            method = getattr(self, self.name)
            method()
        except:
            result.testFailed()
        self.tearDown()
        return result

    def tearDown(self):
        pass

class WasRun(TestCase):
    def setUp(self):
        self.wasRun = None
        self.log = "setUp "

    def testMethod(self):
        self.wasRun = 1
        self.log = self.log + "testMethod "

    def tearDown(self):
        self.log = self.log + "tearDown "

    def testBrokenMethod(self):
        raise Exception

class TestCaseTest(TestCase):
    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert("1 run, 1 failed" == result.summary())

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert("1 run, 0 failed" == result.summary())

    def testTemplateMethod(self):
        self.test = WasRun("testMethod")
        self.test.run()
        assert("setUp testMethod tearDown " == self.test.log)

TestCaseTest("testTemplateMethod").run()
TestCaseTest("testResult").run()
TestCaseTest("testFailedResultFormatting").run()