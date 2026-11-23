import app, json
from google.protobuf.json_format import MessageToJson

try:
    packet = bytes.fromhex(app.BR_HEX)
    print("BR_HEX length:", len(packet))
    proto = app.CguFF_pb2.StartMatch()
    proto.ParseFromString(packet)
    print("Parsed StartMatch proto:")
    print(MessageToJson(proto))
except Exception as e:
    print("Error parsing StartMatch:", e)

# Also let's inspect decode.py
import decode
d = decode.decode_protobuf(bytes.fromhex(app.BR_HEX))
print("Raw protobuf dictionary:")
print(json.dumps(d, indent=2))
