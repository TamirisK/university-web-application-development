FROM golang AS building_stage
COPY ./hello-world.go /
RUN ["go", "build", "/hello-world.go"]

FROM alpine AS running_stage
COPY --from=building_stage /go/hello-world .
ENTRYPOINT [ "./hello-world" ]