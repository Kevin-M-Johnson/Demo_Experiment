#******************
# Test_State_Routines - The routines below are simplle log messages that exercises the varios stated outcomes of tests (Pass/Fail/Warning)
# Created 20220427 - KMJ
#
#******************

def Failing_Test():
    #Posts an error to the test log.
    Log.Error("This is simply a test to demonstrate error execution", "", pmNormal, Project.Variables.LogAtrribFailed)

#@Seed
def Passing_Test():
    #Posts an information message to the test log.
    Log.Message("This is simply a test to demostrate passing execution", "", pmNormal, Project.Variables.LogAtrribInformation)

def Warning_Test():
    #Posts a warning to the test log.
    Log.Warning("This is simply a test to demostrate warning execution", "", pmNormal, Project.Variables.LogAtrribWarning)

#@EventMessage
def Event_Test():
    #Posts an event to the test log.
    Log.Event("This is simply a test to demostrate event message", "", pmNormal, Project.Variables.LogAtrribInformation)
