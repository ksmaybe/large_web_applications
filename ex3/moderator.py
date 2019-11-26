import debate_pb2
import debate_pb2_grpc
import sys


import grpc
def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub=debate_pb2_grpc.CandidateStub(channel)
        if sys.argv[1]=='answer':
            print( stub.Answer(debate_pb2.AnswerRequest(question=sys.argv[2])).answer)
        elif sys.argv[1]=='elaborate':
            go=sys.argv[3:]
            for i in range(len(go)):
                go[i]=int(go[i])
            print(stub.Elaborate(debate_pb2.ElaborateRequest(topic=sys.argv[2],blah_run=go)).answer)
    print(sys.argv)

if __name__=='__main__':
    run()