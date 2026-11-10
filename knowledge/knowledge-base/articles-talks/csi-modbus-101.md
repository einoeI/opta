---
title: "Modbus 101 - Introduction to Modbus"
url: "https://www.csimn.com/CSI_pages/Modbus101.html"
type: vendor-doc
trust: primary
accessed: 2026-11-09
published: unknown
owasp_ot: [5,9]
---

## Summary
A vendor primer on Modbus from Control Solutions Minnesota, Inc.; the page shows Copyright 2020.
It explains RTU, ASCII and TCP framing, the register model, function codes and exceptions.
It is an integrator's introduction and not the Modbus specification, so corroborate protocol-critical details against modbus.org.
It does not discuss security.

## Key facts
- Modbus is master/slave; slaves respond to requests and do not initiate exchanges.
- RTU is usually carried over RS-485, or point-to-point RS-232; speeds of 1200 to 115200 bps are stated, with most devices limited to 38400 bps.
- Modbus ASCII is described as deprecated, rarely used, and absent from the formal specification.
- Modbus TCP wraps RTU-style packets, standardly on port 502; the port can often be reassigned; the IP address is the primary address and the unit ID may be ignored; the checksum is omitted.
- Data types: coil (1-bit read/write), discrete input (1-bit read-only), input register (16-bit read-only), holding register (16-bit read/write).
- Function codes: 1 read coils; 2 read discrete inputs; 3 read holding registers; 4 read input registers; 5 write single coil; 6 write single holding register; 15 write multiple coils; 16 write multiple holding registers.
- Modicon reference ranges: 0x 00001-09999, 1x 10001-19999, 3x 30001-39999, 4x 40001-49999; register 1 corresponds to address 0.
- 32-bit values use consecutive register pairs; default is high-order register first, and some devices swap.
- A single bit in a register cannot be read directly; the full 16-bit register is read and masked.
- Exception replies set the high bit of the function code (0x83 for function 3); codes listed include 1, 2, 3, 4, 6, 10 and 11.
- Only one master is allowed on an RTU network; the protocol limit is stated as 32 devices on a bus, although addressing supports over 250.
- The page does not mention authentication, encryption or access control.

## Verbatim
- "Modbus protocol is defined as a master/slave protocol"
- "The standard port for Modbus TCP is 502, but port number can often be reassigned if desired."

## Relevance
- Basis for a read-only versus write function-code allowlist: codes 1-4 read, codes 5, 6, 15, 16 write.
- Inference: because port 502 can be reassigned, discovery cannot rely on port number alone.
- Inference: a read function can still load a slow device, so read-only is lower risk rather than no risk; this page does not address that.
