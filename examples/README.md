# 📚 Examples

## 📝 Prerequisites

Ensure you have [Rye](https://rye-up.com/) installed on your system. If not, you can install it using the following command:

```bash
curl -sSL https://rye-up.com/install.sh | bash
```

## 🔧 Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/i2y/pydantic-rpc.git
    cd pydantic-rpc/examples
    ```

2. **Install Dependencies with Rye:**

    ```bash
    rye sync
    ```

## 🖥️ gRPC Server Example

### 🔧 Server (`greeting.py`)

A simple gRPC server.

**Usage:**

```bash
rye run python greeting.py
```

### 🔗 Client (`greeter_client.py`)

A gRPC client to interact with the server.

**Usage:**

```bash
rye run python greeter_client.py
```

## ⚡ Asyncio gRPC Server Example

### 🔧 Asyncio Server (`asyncio_greeting.py`)

An asyncio gRPC server using `AsyncIOServer`.

**Usage:**

```bash
rye run python asyncio_greeting.py
```

## 🌐 ASGI Integration (gRPC-Web)

### 🌐 ASGI Application (`greeting_asgi.py`)

Integrate **PydanticRPC** (gRPC-Web) with an ASGI-compatible framework.

**Usage:**

```bash
rye run hypercorn -bind :3000 greeting_asgi:app
```

### 🔗 Client (`greeter_sonora_client.py`)
A gRPC-Web client to interact with the server.

**Usage:**

```bash
rye run python greeter_sonora_client.py
```


## 🌐 WSGI Integration

### 🌐 WSGI Application (`greeting_wsgi.py`)

Integrate **PydanticRPC** (gRPC-Web) with a WSGI-compatible framework.

**Usage:**

```bash
rye run python greeting_wsgi.py
```

### 🔗 Client (`greeter_sonora_client.py`)
A gRPC-Web client to interact with the server.

**Usage:**

```bash
rye run python greeter_sonora_client.py
```


## 🛡️ Custom Interceptor and Running Multiple Services Exxample

### 🔧 Server (`foobar.py`)
A simple gRPC server with custom interceptor and running multiple services.

**Usage:**

```bash
rye run python foobar.py
```

### 🔗 Client (`foobar_client.py`)
A gRPC client to interact with the server.

**Usage:**

```bash
rye run python foobar_client.py
```
