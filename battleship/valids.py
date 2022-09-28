request_validation = {
    "SHOT": {
        "type": "object",
        "properties": {
            "x": {"type": "integer", "maximum": 9, "minimum": 0},
            "y": {"type": "integer", "maximum": 9, "minimum": 0}
        },
        "required": ["x", "y"]
        },

    "SHIP": {
        "type": "object",
        "properties": {
            "x": {"type": "integer", "maximum": 9, "minimum": 0},
            "y": {"type": "integer", "maximum": 9, "minimum": 0},
            "size": {"type": "integer"},
            "direction": {"type": "string"}
        },
        "required": ["x", "y", "size", "direction"]
        },

    "CREATE": {
        "type": "object",
        "properties": {
            "ships": {"type": "array"},
        },
        "required": ["ships"]
        }
}
