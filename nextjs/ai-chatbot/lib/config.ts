export const CONFIG = {
  DEFAULT_MODEL: "deepseek-ai/DeepSeek-V4-Pro",
  ALLOWED_MODELS: [
    "deepseek-ai/DeepSeek-V4-Pro",
    "meta-llama/Llama-3.1-8B-Instruct",
    "meta-llama/Llama-3.1-70B-Instruct"
  ],
  MAX_MESSAGE_COUNT: 50,
  MAX_MESSAGE_LENGTH: 4000,
  MAX_PAYLOAD_SIZE: 150000, // bytes
  ALLOWED_ROLES: ["system", "user", "assistant"]
};
