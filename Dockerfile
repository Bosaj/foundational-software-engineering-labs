# Stage 1: Prepare curated static web and lab artifacts
FROM python:3.15-alpine AS builder

WORKDIR /stage
COPY . .
RUN rm -rf .git .github .pytest_cache __pycache__ tests \
    && printf '{"status":"ok","service":"foundational-software-engineering-labs"}\n' > /stage/healthz

# Stage 2: Hardened non-root unprivileged Nginx runtime
FROM nginxinc/nginx-unprivileged:1.31-alpine AS runtime

WORKDIR /usr/share/nginx/html
COPY --from=builder --chown=101:101 /stage /usr/share/nginx/html

USER 101:101
EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
  CMD wget -q --spider http://127.0.0.1:8080/healthz || exit 1

CMD ["nginx", "-g", "daemon off;"]
