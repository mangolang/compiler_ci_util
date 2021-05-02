
##
## Note: derived files MUST update timestamp on `src/lib.rs` if it is used,
##   otherwise it might not be re-built.
##

FROM python:3.9.4 AS collect_deps

RUN curl 'https://raw.githubusercontent.com/mangolang/compiler/master/Cargo.lock' > 'Cargo.lock'

COPY collect_dependencies.py 'Cargo.toml' ./

RUN python3 collect_dependencies.py 'Cargo.lock' >> Cargo.toml && cat Cargo.toml


FROM clux/muslrust:nightly-2021-04-24 AS build

ENV RUST_BACKTRACE=1

RUN rustup component add rustfmt
RUN rustup component add clippy
RUN cargo install cargo-outdated
RUN cargo install cargo-audit
RUN cargo install cargo-deny
RUN cargo install cargo-tree

# Add the files needed to compile dependencies.
COPY --from=collect_deps Cargo.toml Cargo.toml
COPY --from=collect_deps Cargo.lock Cargo.lock
RUN mkdir -p src  && touch src/lib.rs

# Build the dependencies, remove Cargo files so they have to be re-added.
RUN cat Cargo.toml &&\
    cargo build --workspace --tests &&\
    cargo build --workspace --release &&\
    rm -rf Cargo.toml Cargo.lock src/

