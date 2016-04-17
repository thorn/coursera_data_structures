# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []

    def Process(self, request):
        # write your code here
        # I know, those returns are horrible but please, don't judge me, it was 3h before deadline
        if len(self.finish_time_) == 0:
            self.finish_time_.append(request.arrival_time + request.process_time)
            return Response(False, request.arrival_time)
        elif len(self.finish_time_) < self.size:
            last_packet_finish_time = self.finish_time_[-1]
            current_packet_start_time = max(last_packet_finish_time, request.arrival_time)
            self.finish_time_.append(current_packet_start_time + request.process_time)
            return Response(False, current_packet_start_time)
        else:
            if self.finish_time_[0] > request.arrival_time:
                return Response(True, -1)
            for index, time in enumerate(self.finish_time_):
                if time <= request.arrival_time:
                    del(self.finish_time_[0:index + 1])

                    if len(self.finish_time_) > 0:
                        last_packet_finish_time = max(self.finish_time_[-1], request.arrival_time)
                        self.finish_time_.append(last_packet_finish_time + request.process_time)
                        return Response(False, last_packet_finish_time)
                    else:
                        self.finish_time_.append(request.arrival_time + request.process_time)
                        return Response(False, request.arrival_time)

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
