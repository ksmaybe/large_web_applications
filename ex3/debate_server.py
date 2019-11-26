from concurrent import futures
import logging
import random

import grpc

import debate_pb2
import debate_pb2_grpc
import consultation_pb2
import consultation_pb2_grpc

channel=grpc.insecure_channel('23.236.49.28:50051')
stub=consultation_pb2_grpc.CampaignManagerStub(channel)

class CandidateServicer(debate_pb2_grpc.CandidateServicer):

    def Answer(self, request, context):
        words=['why','what','how','who','when']
        lst=request.question.split(" ")
        if lst[0].lower() in words:
            for i in range(len(lst)):
                if lst[i].lower()=='you':
                    lst[i]='I'
                elif lst[i].lower()=='your':
                    lst[i]='my'
            go=" ".join(lst)
            retort=stub.Retort(consultation_pb2.RetortRequest(original_question=go)).retort
            return debate_pb2.AnswerReply(answer="You asked me "+go+" but I want to say that "+retort)


        else:
            if random.randint(0,1):
                return debate_pb2.AnswerReply(answer="your 3 cent titanium tax goes too far")
            else:
                return debate_pb2.AnswerReply(answer="your 3 cent titanium tax doesn't go too far enough")
    def Elaborate(self, request, context):
        e=request.topic
        ans=""
        if not request.blah_run:
            return debate_pb2.ElaborateReply(answer=e)
        for n in request.blah_run:
            ans+=n*"blah "
            ans+=e
        return debate_pb2.ElaborateReply(answer=ans)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    debate_pb2_grpc.add_CandidateServicer_to_server(CandidateServicer(), server)

    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()