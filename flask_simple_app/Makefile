IMAGE_BASE = flask-simple-app
PROJECTNAME := $(shell basename $(CURDIR))

define HELP
Manage $(PROJECTNAME). Usage:

make run                 - Run $(PROJECTNAME).
make build               - Build $(PROJECTNAME) image.
make ca-certificates     - Generate certificates.
endef
export HELP

.PHONY: all
all: ca-certificates build run

help:
	@echo "$$HELP"

#######################################################################
# OpenSSL: Generate certificates
#######################################################################

.PHONY: ca-certificates
ca-certificates: localhost.key localhost.crt

.PRECIOUS: %.key
%.key:
	openssl genrsa \
		-out $@ \
		2048

.PRECIOUS: %.csr
%.csr: %.key
	openssl req \
		-subj \
		"/C=US/ST=New York/L=New York/O=SomeOrg/CN=example@gmail.com" \
		-new -key $< \
		-out $@

.PRECIOUS: %.crt
%.crt: %.csr %.key
	openssl x509 \
		-req -days 365 \
		-in $*.csr \
		-signkey $*.key \
		-out $@

#######################################################################
# Docker
#######################################################################

.PHONY: run
run:
	docker run \
		--name flask_simple_app \
		--rm \
		-p 7000:7000 \
		$(IMAGE_BASE):latest

.PHONY: build
build:
	docker build -t $(IMAGE_BASE):latest .
