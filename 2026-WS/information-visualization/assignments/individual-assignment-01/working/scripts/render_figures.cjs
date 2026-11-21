// Usage: bundled-node render_figures.cjs /absolute/path/to/node_modules/sharp [figure-name ...]
// Python build_benchmark_figures.py must be run first. Dependency location is explicit.
const path = require('node:path');
const sharp = require(process.argv[2]);
const directory = path.resolve(__dirname, '../figures');

async function main() {
  const requestedNames = process.argv.slice(3);
  for (const name of requestedNames.length ? requestedNames : ['benchmark-white-hat', 'benchmark-black-hat']) {
    if (!/^[a-z0-9-]+$/.test(name)) throw new Error('Invalid figure name');
    const output = path.join(directory, name + '.png');
    const input = path.join(directory, name + '.svg');
    const sourceMetadata = await sharp(input).metadata();
    const targetHeight = Math.round(3200 * sourceMetadata.height / sourceMetadata.width);
    await sharp(input, { density: 225 })
      .resize(3200, targetHeight)
      .withMetadata({ density: 300 })
      .png()
      .toFile(output);
    const metadata = await sharp(output).metadata();
    if (metadata.width !== 3200 || metadata.height !== targetHeight) {
      throw new Error('Unexpected figure dimensions: ' + name);
    }
    console.log(name + ': 3200 × ' + targetHeight + ' PNG, 300 dpi');
  }
}

main().catch(error => { console.error(error); process.exitCode = 1; });
