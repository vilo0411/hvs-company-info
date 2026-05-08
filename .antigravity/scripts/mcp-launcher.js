const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

/**
 * MCP Launcher Script for Google Drive
 * Managed by Antigravity - Workspace Level
 */

async function main() {
  try {
    // 1. Locate project root relative to this script (.antigravity/scripts/mcp-launcher.js)
    const projectRoot = path.resolve(__dirname, '../../');
    const envPath = path.join(projectRoot, '.env');

    if (!fs.existsSync(envPath)) {
      console.error(`[MCP-Launcher] Error: .env file not found at ${envPath}`);
      process.exit(1);
    }

    // 2. Read .env content
    const envContent = fs.readFileSync(envPath, 'utf8');
    const match = envContent.match(/GOOGLE_DRIVE_CREDENTIALS_FILE=(.+)/);
    
    if (!match) {
      console.error("[MCP-Launcher] Error: GOOGLE_DRIVE_CREDENTIALS_FILE not defined in .env");
      process.exit(1);
    }

    const relativeCredsPath = match[1].trim();
    const credsPath = path.resolve(projectRoot, relativeCredsPath);

    if (!fs.existsSync(credsPath)) {
      console.error(`[MCP-Launcher] Error: Credentials file not found at ${credsPath}`);
      process.exit(1);
    }

    const credentialsJson = fs.readFileSync(credsPath, 'utf8');

    // 3. Spawn the actual MCP server
    console.error(`[MCP-Launcher] Starting Google Drive MCP Server using: ${relativeCredsPath}`);
    
    const mcpServer = spawn('npx', ['-y', '@modelcontextprotocol/server-google-drive'], {
      stdio: ['inherit', 'inherit', 'inherit'], // Forward stdin, stdout, stderr
      shell: true,
      env: {
        ...process.env,
        GOOGLE_DRIVE_CREDENTIALS: credentialsJson
      }
    });

    mcpServer.on('exit', (code) => {
      console.error(`[MCP-Launcher] MCP Server exited with code ${code}`);
      process.exit(code);
    });

    // Handle process termination
    process.on('SIGINT', () => mcpServer.kill('SIGINT'));
    process.on('SIGTERM', () => mcpServer.kill('SIGTERM'));

  } catch (err) {
    console.error(`[MCP-Launcher] Fatal Error: ${err.message}`);
    process.exit(1);
  }
}

main();
